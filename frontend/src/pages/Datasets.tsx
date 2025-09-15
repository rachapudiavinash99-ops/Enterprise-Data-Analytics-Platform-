import React, { useState, useCallback, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';
import { UploadCloud, FileText, Loader2, Database, Search } from 'lucide-react';
import axios from 'axios';
import { toast } from 'react-hot-toast';
import Layout from '../components/Layout';

const Datasets = () => {
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploading, setUploading] = useState(false);
  const [datasets, setDatasets] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchDatasets = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/v1/datasets/');
      setDatasets(res.data);
    } catch (err: any) {
      toast.error('Failed to load datasets: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDatasets();
  }, []);

  const onDrop = useCallback(async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    setUploading(true);
    setUploadProgress(0);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const token = localStorage.getItem('token');
      await axios.post('http://127.0.0.1:8000/api/v1/datasets/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `Bearer ${token}`
        },
        onUploadProgress: (progressEvent) => {
          const percentCompleted = Math.round((progressEvent.loaded * 100) / (progressEvent.total || 1));
          setUploadProgress(percentCompleted);
        }
      });
      
      toast.success('Dataset uploaded successfully!');
      fetchDatasets();
    } catch (error: any) {
      toast.error(`Upload error: ${error.message}`);
    } finally {
      setTimeout(() => {
        setUploading(false);
        setUploadProgress(0);
      }, 3000);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, multiple: false });

  return (
    <Layout>
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-xl font-bold text-gray-800 dark:text-white">Datasets</h1>
          <p className="text-sm text-gray-500">Manage and view all your data sources</p>
        </div>
        
        <div 
          {...getRootProps()}
          className="cursor-pointer bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-semibold transition"
        >
          <input {...getInputProps()} />
          {uploading ? `Uploading ${uploadProgress}%` : 'Upload Dataset'}
        </div>
      </div>

      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 overflow-hidden">
        <div className="p-4 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center gap-4">
          <div className="relative w-64">
             <Search className="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
             <input type="text" placeholder="Search datasets..." className="w-full pl-9 pr-3 py-1.5 border border-gray-300 dark:border-gray-600 rounded-md text-sm focus:outline-none focus:border-blue-500 bg-white dark:bg-gray-900" />
          </div>
          <div className="flex gap-3">
             <select className="border border-gray-300 dark:border-gray-600 rounded-md text-sm px-3 py-1.5 bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-300">
               <option>All Types</option>
               <option>CSV</option>
               <option>JSON</option>
             </select>
             <select className="border border-gray-300 dark:border-gray-600 rounded-md text-sm px-3 py-1.5 bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-300">
               <option>All Statuses</option>
               <option>Ready</option>
               <option>Processing</option>
             </select>
          </div>
        </div>

        {loading ? (
          <div className="p-16 flex justify-center">
            <Loader2 className="w-6 h-6 animate-spin text-blue-600" />
          </div>
        ) : datasets.length === 0 ? (
          <div className="p-16 text-center text-gray-500 text-sm">
            No datasets available. Click "Upload Dataset" to add one.
          </div>
        ) : (
          <table className="w-full text-left text-sm">
            <thead className="bg-gray-50 dark:bg-gray-900 text-gray-500 dark:text-gray-400">
              <tr>
                <th className="px-6 py-3 font-semibold">Type</th>
                <th className="px-6 py-3 font-semibold">Name</th>
                <th className="px-6 py-3 font-semibold">Rows</th>
                <th className="px-6 py-3 font-semibold">Columns</th>
                <th className="px-6 py-3 font-semibold">Size</th>
                <th className="px-6 py-3 font-semibold">Status</th>
                <th className="px-6 py-3 font-semibold text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              {datasets.map((ds) => (
                <tr key={ds.id} className="hover:bg-gray-50 dark:hover:bg-gray-800/50">
                  <td className="px-6 py-4">
                    <div className="w-8 h-8 rounded bg-gray-100 flex items-center justify-center text-gray-400 text-xs font-bold border border-gray-200">
                      CSV
                    </div>
                  </td>
                  <td className="px-6 py-4 font-medium text-gray-900 dark:text-white">{ds.name}</td>
                  <td className="px-6 py-4 text-gray-500">{ds.rows}</td>
                  <td className="px-6 py-4 text-gray-500">12</td>
                  <td className="px-6 py-4 text-gray-500">{ds.size}</td>
                  <td className="px-6 py-4">
                    <span className={`px-2 py-1 rounded text-xs font-semibold ${ds.status.toLowerCase() === 'profiled' ? 'bg-green-100 text-green-700' : 'bg-blue-100 text-blue-700'}`}>
                      {ds.status === 'profiled' ? 'Ready' : ds.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <button className="text-gray-400 hover:text-gray-900 transition font-bold px-2">⋮</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </Layout>
  );
};

export default Datasets;

import { useState, useEffect } from 'react'
import Header from './components/Header'
import Jobs from './components/Jobs'
import ActivateJobForm from './components/ActivateJobForm'
import axios from "axios";
import './App.css';

const App = () => {
  const [showActivateJobForm, setShowActivateJobForm] = useState(false)
  const [jobs, setJobs] = useState([])

  useEffect(() => {
    const getJobs = async () => {
      const jobsFromServer = await getJobsFromServer()
      setJobs(jobsFromServer)
    }

    getJobs()
  }, [])

  // Get Jobs
  const getJobsFromServer = async () => {
    const res = await axios.get('http://localhost:5000/jobs')
    if (res.status === 204)
      return []
    const data = res.data
    return data
  }

  // Activate Job
  const activateJob = async (job) => {
    const sec = parseInt(job.interval)
    const res = await axios.put('http://localhost:5000/activate', { method: job.method, seconds: sec });

    const data = await res.data

    setJobs([...jobs, data])
  }

  // Delete Job
  const deactivateJob = async (id) => {
    const res = await axios.put(`http://localhost:5000/deactivate/${id}`, {});

    //We should control the response status to decide if we will change the state or not.
    res.status === 200
      ? setJobs(jobs.filter((job) => job.id !== id))
      : alert('Error Deleting This Job')
  }

  return (
    <div className='container'>
      <Header
        onAdd={() => setShowActivateJobForm(!showActivateJobForm)}
        showForm={showActivateJobForm}
      />

      {showActivateJobForm && <ActivateJobForm onAdd={activateJob} />}
      {jobs.length > 0 ? (
        <Jobs
          jobs={jobs}
          onDelete={deactivateJob}
        />
      ) : (
        'No Active Jobs'
      )}
    </div>
  )
}

export default App


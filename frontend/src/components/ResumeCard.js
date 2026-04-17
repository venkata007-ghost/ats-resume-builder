import React from 'react'

export default function ResumeCard({resume}){
  return (
    <div className="resume-card">
      <h3>{resume.title || 'Untitled'}</h3>
      <p>{resume.summary || ''}</p>
    </div>
  )
}

import React from 'react'

export default function StatsCard({title, value}){
  return (
    <div className="stats-card">
      <strong>{value}</strong>
      <div>{title}</div>
    </div>
  )
}

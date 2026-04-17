import React from 'react'
import { Link } from 'react-router-dom'

export default function Navbar(){
  return (
    <nav>
      <Link to="/">Dashboard</Link> | <Link to="/builder">Builder</Link> | <Link to="/pricing">Pricing"</Link>
    </nav>
  )
}

import { BrowserRouter, Routes, Route } from "react-router-dom";

// Layout
import Navbar from "./components/components_lite/Navbar";
import Footer from "./components/components_lite/Footer";

// Main Pages
import Home from "./components/components_lite/Home";
import Jobs from "./components/components_lite/Jobs";
import Browse from "./components/components_lite/Browse";
import Profile from "./components/components_lite/Profile";

// Auth
import Login from "./components/authentication/Login";
import Register from "./components/authentication/Register";

// Admin
import AdminJobs from "./components/admincomponent/AdminJobs";
import Companies from "./components/admincomponent/Companies";
import CompanyCreate from "./components/admincomponent/CompanyCreate";
import PostJob from "./components/admincomponent/PostJob";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/browse" element={<Browse />} />
        <Route path="/profile" element={<Profile />} />

        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Admin */}
        <Route path="/admin/jobs" element={<AdminJobs />} />
        <Route path="/admin/companies" element={<Companies />} />
        <Route path="/admin/company/create" element={<CompanyCreate />} />
        <Route path="/admin/job/create" element={<PostJob />} />
      </Routes>

      <Footer />
    </>
  );
}

export default App;






















































// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App

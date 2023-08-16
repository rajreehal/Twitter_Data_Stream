import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Tracker from './pages/Tracker'
import Explore from './pages/Explore'
import PagesWONav from './pages/PagesWONav'
import PagesWNav from './pages/PagesWNav'
import { ProtectedRoute } from './ProtectedRoutes'
import './App.css'
import HomePage from './pages/HomePage'

function App() {
  
  return (
    <div>
      <div>
        <Router>
                <Routes>
                    <Route element={<PagesWONav />}>
                      <Route path='' element={<HomePage />}></Route>
                    </Route>
                    <Route element={<PagesWNav />}>
                      <Route path='/Tracker' element={<ProtectedRoute component={ Tracker }/>}></Route>
                      <Route path='/Explore' element={<ProtectedRoute component={ Explore }/>}></Route>
                    </Route>
                      
                </Routes>
        </Router>
      </div>
    </div>
  );
  }

export default App;

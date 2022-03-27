import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./screens/Home";

import Login from "./screens/Login";
import Registration from "./screens/Registration";
import Resources from "./screens/Resources";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index path="/" element={<Home />}></Route>
        <Route path="/resources" element={<Resources />}></Route>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/register" element={<Registration />}></Route>
      </Routes>
    </BrowserRouter>
  );
}


ReactDOM.render(<App />, document.getElementById("root"));
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Signup = () => {
    const navigate = useNavigate();
    const [formData , setFormData] = useState({
        name : "",
        email:"",
        username: "",
        Password: "",

    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
      };
    

    const handleSubmit = (e) => {
        e.prevenDefault();
        const apiurl = "http://localhost:8000/api/signup/";

        fetch(apiurl, {
            method: "POST",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData),
        })
        .then((response) => {
            if (response.status === 201) {
                navigate("./login");
            } 
            else {
                alert('Failed to sign up');
            }
        })
        .catch((error) => {
            console.error("Error signing up:" , error);
        });
    };
    return (
        <div
          className="container d-flex justify-content-center align-items-center vh-100"
          style={{ maxWidth: "700px" }}>
          <form onSubmit={handleSubmit} className="p-4 border shadow w-100">
            <div className="mb-3">
              <label className="form-label">Name:</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                className="form-control"
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Email:</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="form-control"
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Password:</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className="form-control"
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Username:</label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                className="form-control"
                required
              />
            </div>
            <button type="submit" className="btn btn-primary">
              Sign Up
            </button>
          </form>
        </div>
      );
};
export default Signup;
import React , {useState} from 'react';
import {useNavigate} from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const  handleLogin = async = (e) = {
        e.preventDefault();
        try {
            const response = await fetch("http://localhost:3000/api/login/", {
                method:"POST",
                headers: {
                    "Content-Type": "application/json",
                },

                body: JSON.stringify({email: username, password: password}),
            });

            const data = await response.json();
            if (!data.token) {
                alert("Login Failed");
            }
            else {
                localStorage.setItem('token', data.token);
                navigate('/');
            }
            } catch (error) {
                console.log('Error logging in:', error);
            }
        };

        return (
            <div 
            className="container d-flex justify-content-center align-items-center vh-100"
            style={{maxWidth: "700px"}}>
                <form className="p-4 border shadow w-100" onSubmit={handleLogin}>
                    <div>
                        
                    </div>

                </form>
            </div>
        )
    }
} 
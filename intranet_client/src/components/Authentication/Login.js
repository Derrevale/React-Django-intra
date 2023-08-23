import React, { useState } from 'react';
import { login } from '../../services/Api.js';
import { InputGroup, FormControl, Button, Container, Row, Col } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons'; // Importer les icônes pour l'œil et l'œil barré

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const result = await login(username, password);
        if (result.success) {
            console.log("connecter");
        } else {
            setError(result.error);
        }
    };

    return (
        <Container className="mt-5">
            <Row className="justify-content-center">
                <Col md={4}>
                    <h2>Login</h2>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label className="form-label">Username:</label>
                            <FormControl type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Password:</label>
                            <InputGroup>
                                <FormControl
                                    type={showPassword ? 'text' : 'password'}
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    required
                                />
                                <Button variant="outline-secondary" onClick={() => setShowPassword(!showPassword)}>
                                    <FontAwesomeIcon icon={showPassword ? faEyeSlash : faEye} /> {/* Utiliser les icônes Font Awesome */}
                                </Button>
                            </InputGroup>
                        </div>
                        <Button type="submit" variant="primary">Login</Button>
                    </form>
                    {error && <p className="text-danger mt-3">{error}</p>}
                </Col>
            </Row>
        </Container>
    );
};

export default Login;

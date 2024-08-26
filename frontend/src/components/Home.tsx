// Home.tsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
    const [number, setNumber] = useState(0);
    const navigate = useNavigate();

    const handleSubmit = () => {
        navigate(`/result/${number}`);
    };

    return (
        <div className="form-box">
            <h2>Fibonacci Form</h2>
            <div className='form'>
                <div>
                <input 
                    type="number" 
                    value={number} 
                    onChange={e => setNumber(Number(e.target.value))} 
                />
                <button className="btn-primary-block" onClick={handleSubmit}>Generate</button>
                </div>
            </div>
        </div>
    );
};

export default Home;

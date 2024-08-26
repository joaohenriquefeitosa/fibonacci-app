import { useParams, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

function Result() {
    const { number } = useParams<{ number: string }>();
    const [fibonacciNumbers, setFibonacciNumbers] = useState<number[]>([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchFibonacciNumbers = async () => {
            try {
                const response = await fetch(`http://localhost:8000/fibonacci/?n=${number}`);
                if (!response.ok) {
                    throw new Error(`Error: ${response.statusText}`);
                }
                const data = await response.json();
                setFibonacciNumbers(data.result);
            } catch (error) {
                console.error("Failed to fetch Fibonacci numbers:", error);
            }
        };
    
        fetchFibonacciNumbers();
    }, [number]);

    return (
        <div className="form-box">
            <h2>Fibonacci Form</h2>
            <div className='form'>
                <h3>Number: {number}</h3>
                <div className='numbers'>
                    {fibonacciNumbers.map((number, index) => (
                        <div key={index}>{number}</div>
                    ))}
                </div>
                <button className="btn-primary-block" onClick={() => navigate('/')}>Go Back</button>
            </div>
        </div>
    );
};

export default Result;

import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';

const Dashboard = () => {
    const [data, setData] = useState({});

    useEffect(() => {
        axios.get('/api/fraud_stats')
            .then(response => {
                setData({
                    labels: response.data.labels,
                    datasets: [{
                        label: 'Fraud Detection Stats',
                        data: response.data.values,
                        backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    }]
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h2>Fraud Detection Dashboard</h2>
            <Bar data={data} />
        </div>
    );
}

export default Dashboard;

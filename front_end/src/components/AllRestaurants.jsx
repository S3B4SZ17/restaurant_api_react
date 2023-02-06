import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import axios from 'axios';

export default function AllRestaurants (){
  const [data, setData] = useState([]);

  const instance = axios.create({
    baseURL: "http://0.0.0.0:8000",
    });

  useEffect(() => {
    const fetchData = async () => {
      const response = await instance.get('restaurant/getAll');
      setData(response.data);
    };
    fetchData();
  }, []);

  return (
    <Table striped bordered hover variant="dark">
      <thead>
        <tr>
          <th>Name</th>
          <th>Address</th>
          <th>Type</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row) => (
          <tr key={row.id}>
            <td>{row.name}</td>
            <td>{row.address}</td>
            <td>{row.rest_type}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};


import React, { useState, useEffect } from 'react';
import axios from "axios";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';
import toast, { Toaster } from "react-hot-toast";

const RestaurantTypes = ({ options, onChange }) => {
    const [selectedValue, setSelectedValue] = useState(options.id);
  
    const handleChange = (event) => {
      setSelectedValue(event.target.value);
      onChange(event.target.value);
			
    };
  
    return (
      <select value={selectedValue} onChange={handleChange}>
        {options.map((option) => (
          <option key={option.id} value={option.id}>
            {option.name}
          </option>
        ))}
      </select>
    );
};

export default function AddRestaurant (){
  const [name, setName] = useState();
  const [address, setAddress] = useState();
  const [options, setOptions] = useState([]);
  const [selectedOption, setSelectedOption] = useState('');
	const [result, setResult] = useState('');


  const handleName = (event) => {
    setName(event.target.value)
  };

  const handleAddress = (event) => {
    setAddress(event.target.value)
  };


  const instance = axios.create({
    baseURL: "http://0.0.0.0:8000",
    });

	useEffect(() => {
		const fetchOptions = async () => {
			const response = await instance.get('/restaurant/getRestTypes');
			setOptions(response.data);
		};
		fetchOptions();
		}, []);
	
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(selectedOption);

    const data = {
        name: name,
        address: address,
        rest_type: selectedOption
    };

    console.log(data);
    instance
      .post("restaurant/add", data)
      .then((res) => {
        console.log(res.data);
				setResult(res.data.message)
      })
      .catch((error) => console.error(`Error: ${error}`));
  };

    return (
      <div>
        <Card style={{ width: '20rem', margin: '2rem'}}>
          <Card.Body>
          <Card.Title>Add a new Restaurant</Card.Title>
          <Card.Text>
            Calling backend API to add a new restaurant to the DB
          </Card.Text>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicEmail">

              <Form.Label>
                Name:
                <Form.Control type="text" name="name" onChange={handleName} required/>
                Address:
                <Form.Control type="text" name="address" onChange={handleAddress} required/>
                Restaurant type:
                <RestaurantTypes
                    options={options}
                    onChange={(selectedValue) => setSelectedOption(selectedValue)}
                />
              </Form.Label>

              <Button style={{ margin: '5px'}} type="submit" variant="primary">Add</Button>
              <Form.Label>
                Result:
                <Form.Label type="text" name="result" style={{ padding: '15px'}}>[{result}]</Form.Label>
                
              </Form.Label>
            </Form.Group>

          </Form>
        </Card.Body>
      
        </Card>
        
      </div>
    );
}

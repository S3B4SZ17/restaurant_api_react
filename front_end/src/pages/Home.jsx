import React from "react";
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";
import AddRestaurant from "../components/AddRestaurant";
import AllRestaurants from "../components/AllRestaurants"

const Home = () => {
  return (
    <div>
      <Navbar />

      <div style={{padding: '2em'}}> 
        <h1>Welcome to My Restaurants</h1>
      </div>
      <AddRestaurant/>
      <h1>List of all restaurants</h1>
      <AllRestaurants/>
      <Footer />
    </div>
  );
};

export default Home;
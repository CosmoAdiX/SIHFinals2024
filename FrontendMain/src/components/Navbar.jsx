import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-blue-600 bg-opacity-90 text-white py-4 px-6 flex justify-between items-center fixed top-0 left-0 w-screen z-50 backdrop-blur-lg shadow-lg">
      <a href="#home" className="text-2xl font-bold hover:text-blue-300 transition-colors duration-300">
        Logo
      </a>
      <div className="flex space-x-8">
        <a href="#home" className="hover:text-blue-300 transition-colors duration-300">Switch Configuration Panel</a>
        <a href="#about" className="hover:text-blue-300 transition-colors duration-300">Encryption/Decryption</a>
        <a href="#services" className="hover:text-blue-300 transition-colors duration-300">Dashboard</a>
        <a href="#contact" className="hover:text-blue-300 transition-colors duration-300">Contact</a>
      </div>
    </nav>
  );
};

export default Navbar;

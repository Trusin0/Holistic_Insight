<template>
    <div class="user-profile">
      <h2>Username</h2>
      <p>{{ user.username }}</p>
      <h2>Joined</h2>
      <p>{{ user.joined }}</p>
      <a :href="user.permalink">Permalink</a>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      user: Object
    }
  }
  </script>
  
  <style scoped>
  .user-profile {
    border: 1px solid #ddd;
    padding: 16px;
    margin-bottom: 16px;
    border-radius: 8px;
    background-color: #f9f9f9;
    text-align: center;
  }
  
  .user-profile h2 {
    margin: 0;
    font-size: 1.2em;
    color: #555;
  }
  
  .user-profile p {
    margin: 4px 0;
    font-size: 1em;
    color: #333;
  }
  
  .user-profile a {
    color: #3498db;
    text-decoration: none;
  }
  
  .user-profile a:hover {
    text-decoration: underline;
  }
  </style>
  
<template>
    <div class="dashboard">
      <UserProfile :user="user" />
      <table class="test-table">
        <thead>
          <tr>
            <th>Test</th>
            <th>Actions</th>
            <th>Score</th>
            <th>Percentile</th>
          </tr>
        </thead>
        <tbody>
          <TestRow
            v-for="test in tests"
            :key="test.name"
            :test="test"
          />
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import TestRow from './TestRow.vue';
  import UserProfile from './UserProfile.vue';
  
  export default {
    components: {
      TestRow,
      UserProfile
    },
    data() {
      return {
        user: {
          username: 'alicaHKG41',
          joined: '23 hours ago',
          permalink: '#'
        },
        tests: [
          { name: 'react', score: '2.0', percentile: '2.1' },
          { name: 'number', score: null, percentile: null },
          { name: 'shuerte', score: null, percentile: null },
          { name: 'mbti', score: null, percentile: null },
          { name: 'aim', score: null, percentile: null },
          { name: 'color', score: null, percentile: null },
        ]
      };
    }
  }
  </script>
  
  <style scoped>
  .dashboard {
    margin: 20px;
    font-family: Arial, sans-serif;
  }
  
  .test-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 16px;
  }
  
  .test-table th, .test-table td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  .test-table th {
    background-color: #f2f2f2;
    text-align: center;
  }
  </style>
  
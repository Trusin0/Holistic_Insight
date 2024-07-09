<template>
  <div class="dashboard">
    <div class="profile">
      <h2>Username: alicaHKG41</h2>
      <p>Joined: 6 minutes ago</p>
      <a href="#">Permalink</a>
    </div>
    <div class="tests">
      <table>
        <thead>
          <tr>
            <th>Test</th>
            <th>Actions</th>
            <th>Score</th>
            <th>Percentile</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(test, index) in tests" :key="index">
            <td>{{ test.name }}</td>
            <td>
              <button @click="navigate(test.playLink)">Play</button>
              <button @click="navigate(test.statsLink)">Stats</button>
            </td>
            <td>{{ test.score }}</td>
            <td>{{ test.percentile }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="activity-feed">
      <h3>Activity feed</h3>
      <table>
        <thead>
          <tr>
            <th>Test</th>
            <th>Date</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(activity, index) in activities" :key="index">
            <td>{{ activity.test }}</td>
            <td>{{ activity.date }}</td>
            <td>{{ activity.score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tests: [
        { name: 'Sequence Memory', playLink: '#', statsLink: '#', score: '2.0 points', percentile: '2.1%' },
        { name: 'Chimp Test', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
        { name: 'Aim Trainer', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
        { name: 'Typing', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
        { name: 'Verbal Memory', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
        { name: 'Number Memory', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
        { name: 'Visual Memory', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
        { name: 'Reaction Time', playLink: '#', statsLink: '#', score: '?', percentile: '?' },
      ],
      activities: [
        { test: 'Sequence Memory', date: '2024/7/9 16:31:02', score: '2' }
      ]
    };
  },
  methods: {
    navigate(link) {
      // Implement the navigation logic
      window.location.href = link;
    }
  }
};
</script>

<style scoped>
.dashboard {
  font-family: Arial, sans-serif;
  margin: 20px;
}
.profile {
  margin-bottom: 20px;
}
.profile h2 {
  margin: 0;
}
.tests table, .activity-feed table {
  width: 100%;
  border-collapse: collapse;
}
.tests th, .tests td, .activity-feed th, .activity-feed td {
  border: 1px solid #ddd;
  padding: 8px;
}
.tests th, .activity-feed th {
  background-color: #f2f2f2;
}
button {
  background-color: #1E90FF;
  color: white;
  border: none;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  margin: 2px 1px;
  cursor: pointer;
  border-radius: 4px;
}
</style>

``<template>
    <div class="sequence-memory">
      <div class="score">
        <h2>{{ testName | capitalize }}</h2>
        <p>{{ data.points }} points</p>
        <p>{{ data.percentile }}% percentile</p>
        <a @click="play" class="play-button">Play</a>
      </div>
      <div class="charts">
        <h3>{{ testName | capitalize }} Statistics</h3>
        <img :src="plotUrl" alt="Statistics Plot">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      testName: String
    },
    data() {
      return {
        data: {
          points: 0,
          percentile: 0
        },
        plotUrl: ''
      };
    },
    mounted() {
      this.fetchData();
      this.fetchPlot();
    },
    methods: {
      fetchData() {
        fetch(`http://localhost:5000/api/${this.testName}`)
          .then(response => response.json())
          .then(data => {
            this.data.points = data.points;
            this.data.percentile = data.percentile;
          });
      },
      fetchPlot() {
        this.plotUrl = `http://localhost:5000/plot/${this.testName}`;
      },
      play() {
        window.location.href = `/play/${this.testName}`;
      }
    },
    filters: {
      capitalize(value) {
        if (!value) return '';
        value = value.toString();
        return value.charAt(0).toUpperCase() + value.slice(1);
      }
    }
  }
  </script>
  
  <style scoped>
  .sequence-memory {
    font-family: Arial, sans-serif;
  }
  
  .score {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .score h2 {
    margin: 0;
    font-size: 2em;
  }
  
  .score p {
    margin: 5px 0;
    font-size: 1.5em;
  }
  
  .play-button {
    color: white;
    background-color: #3498db;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    cursor: pointer;
  }
  
  .charts {
    margin-top: 20px;
  }
  
  .charts h3 {
    text-align: center;
    margin: 20px 0;
  }
  
  .charts img {
    display: block;
    margin: 0 auto;
    max-width: 100%;
  }
  </style>
  
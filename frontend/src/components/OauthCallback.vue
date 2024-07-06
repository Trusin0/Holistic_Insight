<script>

export default {
  methods: {
    async handleOAuthCallback () {
      const params = new URLSearchParams(window.location.search)
      const code = params.get('code')

      if (code) {
        try {
          const response = await this.$http.get(`http://127.0.0.1:8000/api/oauth?code=${code}`)

          if (response.data.respCode === '000000') {
            window.localStorage.setItem('holistic-insight-token', response.data.token)
            this.$store.state.userInfo = response.data
            // Optionally redirect to another page or indicate success
            this.$router.push({ name: 'index' })
          } else {
            console.error('OAuth failed:', response.data.message)
          }
        } catch (error) {
          console.error('Error during OAuth callback:', error)
        }
      }
    }
  },
  created () {
    this.handleOAuthCallback()
  }
}

</script>

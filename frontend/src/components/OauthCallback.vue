<template>
  <div>
    Redirecting...
  </div>
</template>

<script>
export default {
  created () {
    const query = new URLSearchParams(window.location.search)
    const message = query.get('message')
    const username = query.get('username')
    const id = query.get('id')
    const respCode = query.get('respCode')
    // eslint-disable-next-line camelcase
    const session_key = query.get('session_key')

    // Store the data in localStorage or sessionStorage
    localStorage.setItem('oauth_data', JSON.stringify({
      message,
      username,
      id,
      respCode,
      session_key
    }))

    // Communicate with the opener window
    if (window.opener) {
      window.opener.postMessage({
        type: 'OAUTH_CALLBACK',
        data: {
          message,
          username,
          id,
          respCode,
          session_key
        }
      }, '*')
    }

    // Close the current window
    window.close()
  }
}
</script>

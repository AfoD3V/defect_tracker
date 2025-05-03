<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register" >
        <div>
          <label for="email">Email:</label>
          <input v-model="email" id="email" type="email" required>
        </div>
        <div>
          <label for="password1">Password1:</label>
          <input v-model="password1" id="password1" type="password" required>
        </div>
        <div>
          <label for="password2">Password2:</label>
          <input v-model="password2" id="password2" type="password" required>
        </div>
        <button type="submit">Register</button>
      </form>
      <p v-if="error">{{ error }}</p>
      <p v-if="success">{{ success }}</p>
    </div>
  </template>
  
  <script>
  import { getCSRFToken } from '../store/auth'
  
  export default {
    data() {
      return {
        email: '',
        password1: '',
        password2: '',
        error: '',
        success: ''
      }
    },
    methods: {
      async register() {
        try {
          const response = await fetch('http://localhost:8000/api/register', {
            method: 'POST',
             headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCSRFToken()
                  },
            body: JSON.stringify({
              email: this.email,
              password1: this.password1,
              password2: this.password2,
            }),
            credentials: 'include'
          })
          const data = await response.json()
          if (response.ok) {
            this.success = 'Registration successful! Please log in.'
            setTimeout(() => {
              this.$router.push('/login')
            }, 1000)
          } else {
            this.error = data.error || 'Registration failed'
          }
        } catch (err) {
          this.error = 'An error occurred during registration: ' + err
        }
      }
    }
  }
  </script>
  
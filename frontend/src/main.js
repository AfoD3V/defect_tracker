import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css' // Using the default Vite CSS. Replace with your own global styles.
import router from './router'
import App from './App.vue'
import { useAuthStore } from './store/auth'

const app = createApp(App) //create app by basing on component app

app.use(createPinia()) //state manager
app.use(router) //enabling routing

const authStore = useAuthStore() // Setting CSRF token
authStore.setCsrfToken()

app.mount('#app') //Connecting HTML with Vue
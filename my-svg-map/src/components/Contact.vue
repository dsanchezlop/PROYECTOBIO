<template>
  <div class="hello">
    <br>
    <h1>Contact</h1>
  </div>
  <div>
    <form @submit.prevent="submitForm" class="contact-form">
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="name" required>
    
      <label for="email">Email:</label>
      <input type="email" id="email" v-model="email" required>
    
      <label for="subject">Subject:</label>
      <input type="text" id="subject" v-model="subject" required>
    
      <label for="message">Message:</label>
      <textarea id="message" v-model="message" rows="5" required></textarea>
    
      <button type="submit">Send</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Contact',
  data() {
    return {
      name: '',
      email: '',
      subject: '',
      message: ''
    }
  },
  methods: {
    submitForm() {
      const payload = {
        name: this.name,
        email: this.email,
        subject: this.subject,
        message: this.message
      };
      axios.post('http://127.0.0.1:5000/send-email', payload)
        .then(response => {
          console.log(response);
          alert('Your message has been sent!');
          this.name = '';
          this.email = '';
          this.subject = '';
          this.message = '';
        })
        .catch(error => {
          console.log(error);
          alert('There was an error sending your message. Please try again later.');
        });
    }
  }
}
</script>

<style>
.contact-form {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 5px;
}

.contact-form label {
  font-weight: bold;
  margin-bottom: 10px;
}

.contact-form input[type="text"],
.contact-form input[type="email"],
.contact-form textarea {
  padding: 10px;
  margin-bottom: 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  background-color: #fff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.contact-form textarea {
  height: 150px;
}

.contact-form button[type="submit"] {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

.contact-form button[type="submit"]:hover {
  background-color: #3e8e41;
}
</style>

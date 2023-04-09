const express = require('express')
const bodyParser = require('body-parser')
const nodemailer = require('nodemailer')

const app = express()

// Parse incoming request bodies as JSON
app.use(bodyParser.json())

// Handle POST requests to /submit-form
app.post('/submit-form', (req, res) => {
  const formData = req.body
  // Do something with the form data
  console.log(formData)

  // Create a nodemailer transporter object with your Outlook account details
  const transporter = nodemailer.createTransport({
    service: 'outlook',
    auth: {
      user: 'fertimpact@hotmail.com',
      pass: 'elbichosu.'
    }
  })

  // Define the email message
  const message = {
    from: 'your_email_address@hotmail.com',
    to: 'recipient_email_address@example.com',
    subject: 'New form submission',
    text: `Name: ${formData.name}\nEmail: ${formData.email}\nMessage: ${formData.message}`
  }

  // Send the email
  transporter.sendMail(message, (err, info) => {
    if (err) {
      console.error(err)
      res.status(500).send('Error sending email')
    } else {
      console.log(info)
      res.send('Form submitted and email sent')
    }
  })
})

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000')
})

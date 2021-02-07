const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: "emailSender@gmail.com",
    pass: "passwordSender",
  },
});

const mailOptions = {
  from: "emailSender@gmail.com",
  to: "clientmail1@gmail.com, clientmail2@gmail.com",
  subject: "Invoices due",
  text: "Dudes, we sent to you email",
};

transporter.sendMail(mailOptions, function (error, info) {
  if (error) {
    console.log(error);
  } else {
    console.log("Email sent: " + info.response);
  }
});

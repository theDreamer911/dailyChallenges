const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: "emailSender@gmail.com",
    pass: "passwordSender",
  },
});

const mailOptions = {
  from: "adownlodi@gmail.com",
  to: "scarletf920@gmail.com, handlearn100@gmail.com",
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

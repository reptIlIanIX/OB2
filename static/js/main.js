console.log("Sanity check!");

// new
// Get Stripe publishable key
fetch("/OB2/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
});
$('#add_contact').click(function(event) {
  let first_name = ["Ana", "Beatriz", "Carlos", "Eduardo", "Regis", "Guilherme", "Gustavo", "Arthur", "Simone", "Leticia"]
  let last_name = ['Richter', 'Yeargin', 'Blackwood', 'Smith', 'Peck', 'Nguyen', 'Cradle', 'Mckelvey', 'Sumrall', 'Clemmer', 'Bromley', 'Cothren', 'Ovitt', 'Steppig', 'Coles', 'Drain', 'Baker', 'Humphries', 'Suggs', 'Deldonno']

  function getFirstname() {
    // Escolhe um nome
    return first_name[Math.floor(Math.random() * first_name.length)]
  }

  function getLastname() {
    // Escolhe um nome
    return last_name[Math.floor(Math.random() * last_name.length)]
  }

  function getPhone() {
    let vphone = Math.floor((Math.random() * 1000000000) + 1)
    vphone = vphone.toString()
    vphone = ''.concat(vphone.slice(0,4), '-', vphone.slice(4,-1))
    return vphone
  }

  let fname = getFirstname()
  let lname = getLastname()
  let email = ''.concat(fname.toLowerCase(), '.', lname.toLowerCase(), '@email.com')
  let phone = getPhone()
  // Define o nome no campo first_name
  $('#id_first_name').val(fname);
  // Define o sobrenome no campo last_name
  $('#id_last_name').val(lname);
  // Define o email
  $('#id_email').val(email);
  $('#id_phone').val(phone);
  console.log(fname);
});
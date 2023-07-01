<!DOCTYPE html>
<html>
<head>
  <title>Main Menu Website</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    header {
      background-color: #333;
      color: #fff;
      padding: 10px;
    }

    nav ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
    }

    nav ul li {
      display: inline-block;
      margin-right: 10px;
    }

    nav ul li a {
      color: #fff;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <header>
<span id="username"></span>!</p>

  <script>
    // Retrieve the username from the URL parameters and display it
    const params = new URLSearchParams(window.location.search);
    const username = params.get('username');
    document.getElementById('username').textContent = username;
  </script>
    <nav>
      <ul id="main-menu">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </header>

  <h1>Welcome to the Main Menu Website</h1>
  <p>This is a basic website with a main menu implemented in JavaScript.</p>

  <!-- Additional content goes here -->

  <script>
    // Add active class to the clicked menu item
    var menuItems = document.querySelectorAll('#main-menu li');
    menuItems.forEach(function(item) {
      item.addEventListener('click', function() {
        menuItems.forEach(function(item) {
          item.classList.remove('active');
        });
        this.classList.add('active');
      });
    });
  </script>
</body>
</html>
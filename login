<!DOCTYPE html>
<html>
<head>
  <title>Login Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    
    .container {
      width: 300px;
      margin: 100px auto;
      padding: 20px;
      background-color: #f4f4f4;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    
    h2 {
      text-align: center;
    }
    
    .form-group {
      margin-bottom: 15px;
    }
    
    .form-group label {
      display: block;
      margin-bottom: 5px;
    }
    
    .form-group input {
      width: 100%;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 3px;
    }
    
    .form-group input[type="submit"] {
      background-color: #333;
      color: #fff;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Login</h2>
    <form action="main.html" method="POST">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" name="Haya" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" name="Amma@1234" required>
      </div>
      <div class="form-group">
       </div>
    </form>
  </div>
</body>
</html>

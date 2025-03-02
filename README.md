<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Yash's Domain</title>
    <style>
        body {
            background-color: #1e1e1e;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 3em;
            text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
            margin-top: 20px;
        }
        .container {
            position: relative;
            display: inline-block;
            margin-top: 50px;
        }
        img {
            border: 2px solid #00ff00;
            border-radius: 10px;
            box-shadow: 0 0 20px #00ff00;
        }
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.5s;
        }
        .container:hover .overlay {
            opacity: 1;
        }
        .overlay-text {
            color: #00ff00;
            font-size: 1.5em;
            text-shadow: 0 0 10px #00ff00;
        }
    </style>
</head>
<body>

<div class="container">
    <img alt="Coder GIF" height="350" width="550" src="https://granroyalleigarape.com.br/wp-content/uploads/2021/05/programmer.gif" />
    <div class="overlay">
        <div class="overlay-text">Welcome to the Code Realm</div>
    </div>
</div>

<h1>Hey, It's Yash</h1>

</body>
</html>

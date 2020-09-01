<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <title>ToDO</title>

    <style>
        .ob-straneh {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
        }

        .card-text {
            margin-bottom: 0;
        }

        .card {
            margin-top: 1em;
        }


        .gumb-odjava {
            position: absolute;
            top: 1em;
            right: 2em;
        }

        .gumb-nazaj {
            position: absolute;
            top: 1em;
            left: 2em;
        }

        form.card {
            margin-top: 2em;
            margin-bottom: 2em;
            padding: 1em;
        }

        form h3 {
            margin-bottom: 0.5em;
            font-weight: normal;
        }
        .sredina {
            margin-left: auto;
            margin-right: auto;
        }

        .pod-naslovom {
            margin-top: 1em;
            margin-bottom: 1em;
        }

        .btn-group .selected {
            text-decoration: underline;
        }

        .btn-izbrisi {
            float: right;
            width: fit-content;
            position: absolute;
            top: 0.65em;
            right: 0.8em;
            font-size: 0.7em;
        }
    </style>
</head>
<body>
    <div class="text-center container">
        {{!base}}
    </div>
</body>
</html>
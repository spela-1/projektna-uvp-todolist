%rebase('base.tpl')

<h1>Prijava</h1>
<form action="/prijava" method="POST">
  <div class="form-group">
    <label for="username">Uporabniško ime</label>
    <input type="text" class="form-control" id="username" name="ime">
  </div>
  <div class="form-group">
    <label for="geslo">Password</label>
    <input type="password" class="form-control" id="geslo" name="geslo">
  </div>
  <button type="submit" class="btn btn-primary">Prijava</button>
  <br>
  <a href="/sign-up">Ustvari nov računa</a>
</form>
%rebase('base.tpl')

<h1>Nov račun</h1>
<form action="/registracija" method="POST">
  <div class="form-group">
    <label for="username">Uporabniško ime</label>
    <input type="text" class="form-control" id="username" name='ime'>
  </div>
  <div class="form-group">
    <label for="geslo">Password</label>
    <input type="password" class="form-control" id="geslo" name='geslo'>
  </div>
  <button type="submit" class="btn btn-primary">Ustvari račun</button>
  <br>
  <a href="/login">Prijavi se</a>
</form>
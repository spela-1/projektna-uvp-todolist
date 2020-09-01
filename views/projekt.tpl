%rebase('base.tpl')

<a href="/odjava" class="btn btn-outline-primary btn-sm gumb-odjava">Odjava</a>
<a href="/projekti/tvoji" class="btn btn-outline-primary btn-sm gumb-nazaj">Vsi projekti</a>
<h1>{{projekt.ime}}</h1>
<div class="pod-naslovom ob-straneh text-muted">
    <div>
        % if len(projekt.deljeno_z) > 0:
            <em>Deljeno z:</em> 
                % for oseba in projekt.deljeno_z:
                    {{oseba}}
                % end
        % end
    </div>
    <form class="form-inline form-small align-items-center text-center" action="/deli/{{ime_lastnika}}/{{projekt.id}}" method="POST">
        <div class="sredina">
            <input type="text" class="form-control" id="oseba" name="oseba" placeholder="deli z osebo">
            <button type="submit" class="btn btn-outline-primary">+</button>
        </div>
    </form>
</div>
<div class="">
    % for naloga in projekt.seznam_nalog:
        <div class="card">
            <div class="card-body ob-straneh">
                <h5 class="card-title">{{naloga.tekst}}</h5>
                <a href="/opravi-nalogo/{{ime_lastnika}}/{{projekt.id}}/{{naloga.id}}" class="btn {{'btn-primary' if naloga.opravljeno else 'btn-outline-primary'}}">&#10003;</a>
            </div>
            <div class="card-footer text-muted ob-straneh">
                <span><em>{{'.'.join([str(i) for i in naloga.datum[::-1]])}}</em> {{'{}:{:02}'.format(naloga.ura[0], naloga.ura[1]) if len(naloga.ura) > 0 else ''}}</span>
                <span><em>Prioriteta:</em>{{naloga.prioriteta}}</span>
            </div>
        </div>
    % end
</div>

<form class="text-left card" action="/nova-naloga/{{ime_lastnika}}/{{projekt.id}}" method="POST" >
    <h3>Nova naloga</h3>
    <div class="form-group">
        <input type="text" class="form-control" id="ime" name="tekst" placeholder="naloga">
    </div>
    <div class="form-group">
        <label for="datum">Datum</label>
        <input type="date" class="form-control" id="datum" name="datum">
    </div>
    <div class="form-group">
        <label for="ura">Ura</label>
        <input type="time" class="form-control" id="ura" name="ura">
    </div>
    <div class="form-group">
        <label for="prioriteta">Prioriteta</label>
        <select class="form-control" id="prioriteta" name="prioriteta">
            <option>0</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
        </select>
    </div>
    <button type="submit" class="btn btn-primary">Dodaj</button>
</form>
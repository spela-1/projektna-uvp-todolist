%rebase('base.tpl')

<a href="/odjava" class="btn btn-outline-primary btn-sm gumb-odjava">Odjava</a>
<h1>Tvoji projekti</h1>
<div class="btn-group pod-naslovom" role="group">
    <a href="/projekti/tvoji" class="btn btn-secondary {{'selected' if izbira == 'tvoji' else ''}}">Tvoji projekti</a>
    <a href="/projekti/deljeni" class="btn btn-secondary {{'selected' if izbira == 'deljeni' else ''}}">Deljeni projekti</a>
    <a href="/projekti/danes" class="btn btn-secondary {{'selected' if izbira == 'danes' else ''}}">Naloge za danes</a>
</div>
<div class="">
    % for projekt, ime in zip(projekti, imena_uporabnikov):
        <div class="card">
            <h5 class="card-header">{{projekt.ime}}</h5>
            % if izbira == 'tvoji':
                <a href="/izbrisi-projekt/{{projekt.id}}" class="btn btn-outline-primary btn-izbrisi" >Izbriši</a>
            % end
            <div class="card-body ob-straneh">
                <p class="card-text">{{len(projekt.seznam_nalog)}} naloge</p>
                <a href="/projekt/{{ime}}/{{projekt.id}}" class="btn btn-primary">Odpri</a>
            </div>
            % if len(projekt.deljeno_z) > 0:
                <div class="card-footer text-muted">
                    Deljeno z: 
                    % for oseba in projekt.deljeno_z:
                        {{oseba}}
                    % end
                </div>
            % end
        </div>
    % end
</div>

% if izbira == 'tvoji':
<form class="text-left card" action="/nov-projekt" method="POST" >
    <h3>Nov projekt</h3>
    <div class="form-group">
        <input type="text" class="form-control" id="ime" name="ime" placeholder="projekt">
    </div>
    <button type="submit" class="btn btn-primary">Dodaj</button>
</form>
% end
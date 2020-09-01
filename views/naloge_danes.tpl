%rebase('base.tpl')

<a href="/odjava" class="btn btn-outline-primary btn-sm gumb-odjava">Odjava</a>
<a href="/projekti/tvoji" class="btn btn-outline-primary btn-sm gumb-nazaj">Vsi projekti</a>
<h1>Današnje naloge</h1>
<div class="">
    % for naloga in naloge:
        <div class="card">
            <div class="card-body ob-straneh">
                <h5 class="card-title">{{naloga.tekst}}</h5>
                <a href="/opravi-nalogo/{{ime_lastnika}}/{{naloga.id_pr}}/{{naloga.id}}" class="btn {{'btn-primary' if naloga.opravljeno else 'btn-outline-primary'}}">&#10003;</a>
            </div>
            <div class="card-footer text-muted ob-straneh">
                <span><em>{{'.'.join([str(i) for i in naloga.datum[::-1]])}}</em> {{'{}:{:02}'.format(naloga.ura[0], naloga.ura[1]) if len(naloga.ura) > 0 else ''}}</span>
                <span><em>Prioriteta:</em>{{naloga.prioriteta}}</span>
            </div>
        </div>
    % end
</div>
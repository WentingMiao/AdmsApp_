import django_tables2 as tables
from .models import Activity


class activityTable(tables.Table):
    title = tables.TemplateColumn(
        '  <a href="{% url \'activitiy_details\' pk=record.id %}">{{record.title}}</a>',
        verbose_name='Title'
    )

    status = tables.TemplateColumn(
        ' {% now "Y-m-d" as todays_date %} {% if todays_date > record.hold_time|date:"Y-m-d" %} <span class="badge badge-secondary">Finished</span> {% else %} {% if record.registered_members.count >= record.expected_number%}<span class="badge badge-danger">Full</span> {% else %}  <span class="badge badge-success">Available</span> {% endif %} {% endif%}',
        orderable=False,
        verbose_name='Status'
    )

    deadline = tables.DateTimeColumn(format ='M d Y, h:i A')
    # delete = tables.TemplateColumn(
    #     ' <form action="{% url \'activity_delete\' pk=record.id %}" method="post">{% csrf_token %}<input type="hidden" name="_method" value="delete"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-info btn-xs">Delete</button></form>',
    #     orderable=False,
    #     verbose_name=''
    # )
    class Meta:
        model = Activity
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ("title","name", "department", "short_descipt",'deadline') 



class applicationTable(tables.Table):
    title = tables.TemplateColumn(
        '  <b>{{record.title}}</b>',
        verbose_name='Title'
    )
    status = tables.TemplateColumn(
        ' {% now "Y-m-d" as todays_date %} {% if record.passed %} <span class="badge badge-success">Passed</span> {% else %} {% if record.comment %}<span class="badge badge-danger">Fail</span> {% else %}  <span class="badge badge-warning">Processing</span> {% endif %} {% endif%}',
        orderable=False,
        verbose_name='Status'
    )

    
    check = tables.TemplateColumn(
        ' <form action="{% url \'activitiy_details\' pk=record.id %}" method="post">{% csrf_token %}<button type="submit" class="btn btn-info btn-xs">Check</button></form>',
        orderable=False,
        verbose_name=''
    )
    comment_user = tables.TemplateColumn(
        '  <p style="color:#FF0000">{{record.comment_user}}</p>',
        verbose_name='Inspector',
        orderable=False,
    )
    class Meta:
        model = Activity
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ("title","name", "department", "comment",'comment_user','status','check') 


class selfApplicationTable(tables.Table):
    title = tables.TemplateColumn(
        '  <b>{{record.title}}</b>',
        verbose_name='Title'
    )
    status = tables.TemplateColumn(
        ' {% now "Y-m-d" as todays_date %} {% if record.passed %} <span class="badge badge-success">Passed</span> {% else %} {% if record.comment %}<span class="badge badge-danger">Fail</span> {% else %}  <span class="badge badge-warning">Processing</span> {% endif %} {% endif%}',
        orderable=False,
        verbose_name='Status'
    )
    check = tables.TemplateColumn(
        ' <form action="{% url \'activitiy_details\' pk=record.id %}" method="post">{% csrf_token %}<button type="submit" class="btn btn-info btn-xs">Check</button></form>',
        orderable=False,
        verbose_name=''
    )
    comment_user = tables.TemplateColumn(
        '  <p style="color:#FF0000">{{record.comment_user}}</p>',
        verbose_name='Inspector',
        orderable=False,
    )

    class Meta:
        model = Activity
        attrs = {"class": "table table-bordered table-hover dataTable"}
        fields = ("title","name",  "comment",'comment_user','status','check') 

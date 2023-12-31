# Generated by Django 4.2.7 on 2023-12-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="stage",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted at"
            ),
        ),
        migrations.AddField(
            model_name="stage",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Active"), (1, "Closed"), (2, "Slowed")],
                default=0,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="userproject",
            name="role",
            field=models.IntegerField(
                choices=[(0, "Stage Owner"), (1, "Member"), (2, "Project Manager")],
                default=2,
                verbose_name="Role",
            ),
        ),
    ]

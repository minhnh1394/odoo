from odoo import api,fields, models


class Info(models.Model):
    _name='student.info'
    _description='Infomation'  

    @api.multi
    @api.depends('gpa')
    def set_classification(self):
        for info in self:
            if info.gpa:
                if info.gpa>=9.5:
                    info.classification='excellent'
                else:
                    if info.gpa>=6.5:
                        info.classification='good'
                    else:
                        if info.gpa>=6:
                            info.classification='average'
                        else:
                            info.classification='poor'


    name = fields.Char('Fullname',required=True)
    student_id= fields.Char ('Student\'s id',required=True)
    identification_number= fields.Char ('Passport')
    gender= fields.Selection([('male','Male'),('female','Female'),('other','Other')],default='male',string='Chose Gender')
    image=fields.Binary('Student\'s image')
    date_of_birth= fields.Date('Date of birth')
    address= fields.Text('Student\'s address')
    phone= fields.Char('Phone number')
    gpa=fields.Float('Current GPA')
    classification=fields.Selection([('excellent','Excellent'), ('good','Good'),('average','Average'),('poor','Poor')],default='poor',string='Classification',compute='set_classification')
    notes= fields.Char('Internal notes')


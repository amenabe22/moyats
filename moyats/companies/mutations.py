from unicodedata import name
import graphene
from core.models import BaseContact
from accounts.models import BaseUser, Address
from graphene_file_upload.scalars import Upload
from .models import Company, CompanyContact, CompanyContactStatus, CompanyStatus
from .inputs import CompanyContactInput, CompanyPrimaryInfoUpdateInput, ContactPrimaryInfoUpdateInput
from graphql_jwt.decorators import login_required
from .types import CompanyContactType, CompanyType
from .inputs import CompanyInput


class AddCompanyContact(graphene.Mutation):
    class Arguments:
        input = CompanyContactInput()

    ok = graphene.Boolean()
    contact = graphene.Field(CompanyContactType)

    @login_required
    def mutate(self, info, input: CompanyContactInput, **kwargs):
        org = info.context.user.organizations.first()
        addr = None
        address = Address.objects.filter(
            country=input.country, city=input.city)
        if not address.exists():
            addr = Address.objects.create(
                country=input.country, city=input.city)
        else:
            addr = address.first()
        company = Company.objects.filter(
            company_id=input.company, organization=org)

        if not company.exists():
            raise Exception("invalid input")

        contact = BaseContact.objects.create(
            cell_number=input.phones.cell_phone
        )
        default_status = CompanyContactStatus.objects.filter(
            initial=True
        )
        company_contact = CompanyContact.objects.create(
            first_name=input.first_name,
            last_name=input.last_name,
            email=input.email,
            organization=org,
            company=company.first(),
            address=addr,
            phones=contact,
            status=default_status.first(),
        )
        return AddCompanyContact(ok=True, contact=company_contact)


class ContactPrimaryInfoUpdateMutation(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = ContactPrimaryInfoUpdateInput()

    def mutate(self, info, input: ContactPrimaryInfoUpdateInput, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=input.contact)
        if not contacts.exists():
            raise Exception("contact not found")
        addr = None
        address = Address.objects.filter(
            country=input.country, city=input.city)
        contact = BaseContact.objects.create(
            cell_number=input.phones.cell_phone
        )

        if not address.exists():
            addr = Address.objects.create(
                country=input.country, city=input.city)
        else:
            addr = address.first()
        contacts.update(first_name=input.name.first_name if input.name.first_name else contacts.first().first_name,
                        last_name=input.name.last_name if input.name.last_name else contacts.first().last_name,
                        phones=contact,
                        address=addr,
                        )
        return ContactPrimaryInfoUpdateMutation(response=True)


class CompanyContactStatusUpdate(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        status = graphene.Int()

    @login_required
    def mutate(self, info, contact, status, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")
        stat = CompanyContactStatus.objects.filter(id=status)
        if not stat.exists():
            raise Exception("status not found")

        contacts.update(status=stat.first())
        return CompanyContactStatusUpdate(response=True)


class UpdateContactCompany(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        company = graphene.String()
        department = graphene.String()

    @login_required
    def mutate(self, info, contact, company, department, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")
        comp = Company.objects.filter(company_id=company)
        if not comp.exists():
            raise Exception("company not found")

        contacts.update(company=comp.first(), department=department)
        return UpdateContactCompany(response=True)


class UpdateContactReport(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        report_to = graphene.Int()

    @login_required
    def mutate(self, info, contact, report_to, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")
        report = BaseUser.objects.filter(id=report_to)
        if not report.exists():
            raise Exception("user not found")

        contacts.update(contact_reports_to=report.first())
        return UpdateContactReport(response=True)


class UpdateContactNote(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        contact = graphene.String()
        note = graphene.String()

    @login_required
    def mutate(self, info, contact, note, **kwargs):
        contacts = CompanyContact.objects.filter(
            company_contact_id=contact)
        if not contacts.exists():
            raise Exception("contact not found")

        contacts.update(notes=note)
        return UpdateContactNote(response=True)


class UpdateCompanyPrimary(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        input = CompanyPrimaryInfoUpdateInput()

    @login_required
    def mutate(self, info, input: CompanyPrimaryInfoUpdateInput, **kwargs):
        company = Company.objects.filter(
            company_id=input.company)
        if not company.exists():
            raise Exception("company not found")
        contact = BaseContact.objects.create(
            cell_number=input.phones.cell_phone
        )
        addr = None
        address = Address.objects.filter(
            country=input.country, city=input.city)
        if not address.exists():
            addr = Address.objects.create(
                country=input.country, city=input.city)
        else:
            addr = address.first()

        company.update(
            website=input.website,
            name=input.name if input.name else company.first().name,
            phones=contact, address=addr)
        return UpdateContactNote(response=True)


class UpdateCompanyStatus(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        company = graphene.String()
        status = graphene.Int()

    @login_required
    def mutate(self, info, company, status, ** kwargs):
        company = Company.objects.filter(
            company_id=company)
        if not company.exists():
            raise Exception("company not found")
        stat = CompanyStatus.objects.filter(id=status)
        if not stat.exists():
            raise Exception("status not found")

        company.update(company_status=stat.first())
        return UpdateContactNote(response=True)


class UpdateCompanyNotes(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        company = graphene.String()
        note = graphene.String()

    @login_required
    def mutate(self, info, company, note, **kwargs):
        comp = Company.objects.filter(company_id=company)
        if not comp.exists():
            raise Exception("company not found")

        comp.update(notes=note)
        return UpdateCompanyNotes(response=True)


class AddCompanyAttachments(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        file = Upload(required=True)
        company = graphene.String()
        filename = graphene.String()
        is_resume = graphene.Boolean()

    @login_required
    def mutate(self, info, file, company, filename, is_resume, **kwargs):
        comp = Company.objects.filter(company_id=company)
        if not comp.exists():
            raise Exception("company not found")
        comp.first().attachments.create(file=file, filename=filename, is_resume=is_resume)
        return AddCompanyAttachments(response=True)


class AddCompany(graphene.Mutation):
    response = graphene.Field(CompanyType)

    class Arguments:
        input = CompanyInput()

    @login_required
    def mutate(self, info, input: CompanyInput, **kwargs):
        org = info.context.user.organizations.first()
        contact = BaseContact.objects.create(
            cell_number=input.phones.cell_phone
        )
        addr = None
        address = Address.objects.filter(
            country=input.country, city=input.city)
        if not address.exists():
            addr = Address.objects.create(
                country=input.country, city=input.city)
        else:
            addr = address.first()
        default_status = CompanyStatus.objects.filter(
            initial=True
        )
        company = Company.objects.create(
            website=input.website,
            name=input.name,
            company_status=default_status.first(),
            organization=org,
            phones=contact, address=addr)
        return AddCompany(response=company)



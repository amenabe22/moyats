import graphene
import graphql_jwt
from core.query import CoreQuery
from accounts.query import AccountsQuery
from organizations.mutations import CreateOrganization
from accounts.mutation import AddNewUser, VerifyEmail, SocialMediaRegistration
from organizations.query import OrganizationQuery
from joborders.query import JobOrderQuery


class Query(AccountsQuery, CoreQuery, OrganizationQuery, JobOrderQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    base_user_login = graphql_jwt.ObtainJSONWebToken.Field()
    base_user_logout = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    check_email_verification = VerifyEmail.Field()
    register = AddNewUser.Field()
    social_auth = SocialMediaRegistration.Field()
    setup_account = CreateOrganization.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

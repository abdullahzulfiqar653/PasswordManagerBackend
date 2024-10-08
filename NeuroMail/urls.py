from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from NeuroMail.views import (
    EmailListCreateView,
    EmailExtensionListView,
    EmailRetrieveDeleteView,
    EmailAiTemplateListView,
    RephraseEmailCreateView,
    EmailExistenceCheckView,
    MailboxEmailListCreateView,
    MailboxEmailRetrieveUpdateView,
    MailboxEmailTrashView,
)

from main.views import (
    UserSignInView,
    UserSignUpView,
    UserProfileRetrieveUpdateDeleteView,
)

urlpatterns = [
    # =====================================================
    # User
    # =====================================================
    path("user/token/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path("user/generate-token/", UserSignInView.as_view(), name="generate-token"),
    path(
        "user/generate-pass-phrase/",
        UserSignUpView.as_view(),
        name="generate-pass-phrase",
    ),
    # =====================================================
    # Email
    # =====================================================
    path(
        "emails/existance/verify/",
        EmailExistenceCheckView.as_view(),
        name="email-existance-verify",
    ),
    path("emails/", EmailListCreateView.as_view(), name="email-list-create"),
    path(
        "emails/extensions/",
        EmailExtensionListView.as_view(),
        name="email-extension-list",
    ),
    path(
        "emails/<str:pk>/",
        EmailRetrieveDeleteView.as_view(),
        name="email-retrive-delete",
    ),
    path(
        "emails/ai/templates/",
        EmailAiTemplateListView.as_view(),
        name="email-ai-templates-list",
    ),
    path(
        "emails/ai/rephrase/",
        RephraseEmailCreateView.as_view(),
        name="rephrase-email-create",
    ),
    # =====================================================
    # Email
    # =====================================================
    path(
        "mailbox/emails/",
        MailboxEmailListCreateView.as_view(),
        name="mailbox-email-list-create",
    ),
    path(
        "mailbox/emails/trash/",
        MailboxEmailTrashView.as_view(),
        name="mailbox-email-trash",
    ),
    path(
        "mailbox/emails/<str:pk>/",
        MailboxEmailRetrieveUpdateView.as_view(),
        name="mailbox-email-retrieve-update",
    ),
    # =====================================================
    # Profile
    # =====================================================
    path(
        "profile/pictures/",
        UserProfileRetrieveUpdateDeleteView.as_view(),
        name="user-profile-retrieve-update-delete",
    ),
]

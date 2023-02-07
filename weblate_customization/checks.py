# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Simple quality check example."""

from django.utils.translation import ugettext_lazy as _
from weblate.checks.base import TargetCheck


class FooCheck(TargetCheck):
    """Check whether "foo" string is not present in the target."""

    # Used as identifier for check, should be unique
    # Has to be shorter than 50 chars
    check_id = "foo"

    # Short name used to display failing check
    name = _("Foo check")

    # Description for failing check
    description = _("Your translation is foo")

    def check_single(self, source, target, unit):
        """Real check code."""
        return "foo" in target

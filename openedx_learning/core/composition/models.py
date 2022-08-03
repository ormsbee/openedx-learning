"""
THIS IS NON-FUNCTIONING scratch code at the moment.

There are broadly three types of UserPartitions:

1. Partitions that are global to a LearningContextType.
2. Partitions that are specific to a LearningContextVersion.

"""
from django.db import models

from openedx_learning.lib.fields import hash_field, identifier_field, immutable_uuid_field

from ..itemstore.models import ItemVersion
from ..publishing.models import LearningContext, LearningContextVersion


class Segment(models.Model):
    """
    Segments are the lowest renderable component in a learning context.

    Most of the layout of a Segment follows closely to that of an item. The biggest
    difference is that a SegmentVersion will "contain" a list of orered ItemVersions.
    """

    uuid = immutable_uuid_field()
    learning_context = models.ForeignKey(LearningContext, on_delete=models.CASCADE)

    # Mutable app defined identifier.
    identifier = identifier_field()

    created = manual_date_time_field()
    modified = manual_date_time_field()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["learning_context", "identifier"],
                name="segment_uniq_lc_identifier",
            )
        ]

    def __str__(self):
        return f"{self.identifier}"


class SegmentVersion(models.Model):
    """
    A particular version of a Segment.

    A new version should be created when there is a change to the set of items in
    a segment.

    Question for Dave: Why should this map to item versions instead of item? When would we
    reference the Item model directly?
    """

    uuid = immutable_uuid_field()

    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)

    segment_items = models.ManyToManyField(
        ItemVersion,
        through="SegmentVersionItemVersion",
        related_name="segment_versions",
    )

    learning_context_versions = models.ManyToManyField(
        LearningContextVersion,
        through="LearningContextVersionSegmentVersion",
        related_name="segment_versions",
    )


class LearningContextVersionSegmentVersion(models.Model):
    learning_context_version = models.ForeignKey(
        LearningContextVersion, on_delete=models.CASCADE
    )
    segment_version = models.ForeignKey(SegmentVersion, on_delete=models.RESTRICT)

    segment = models.ForeignKey(Segment, on_delete=models.RESTRICT)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["learning_context_version", "segment_version"],
                name="lcvsv_uniq_lcv_segment_version",
            ),
            models.UniqueConstraint(
                fields=["learning_context_version", "segment"],
                name="lcvsv_uniq_lcv_segment",
            ),
        ]


class SegmentVersionItemVersion(models.Model):
    segment_version = models.ForeignKey(SegmentVersion, on_delete=models.CASCADE)
    item_version = models.ForeignKey(ItemVersion, on_delete=models.RESTRICT)

    order_num = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["segment_version", "order_num"],
                name="sviv_uniq_segment_item_order",
            )
        ]

# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model to handle all operations related to Payment Transaction."""
from datetime import datetime

from sqlalchemy import ForeignKey

from .base_model import BaseModel
from .db import db, ma


class PaymentTransaction(db.Model, BaseModel):  # pylint: disable=too-few-public-methods
    """This class manages all of the base data about Payment Transaction."""

    __tablename__ = 'payment_transaction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_code = db.Column(db.String(10), ForeignKey('status_code.code'), nullable=False)
    payment_id = db.Column(db.Integer, ForeignKey('payment.id'), nullable=False)
    redirect_url = db.Column(db.String(200), nullable=False)
    pay_system_url = db.Column(db.String(500), nullable=False)

    transaction_start_time = db.Column(db.DateTime, default=datetime.today(), nullable=False)
    transaction_end_time = db.Column(db.DateTime, default=datetime.today(), nullable=True)

    @classmethod
    def find_by_id(cls, identifier: int):
        """Return a Payment Transaction by id."""
        return cls.query.get(identifier)


class PaymentTransactionSchema(ma.ModelSchema):
    """Main schema used to serialize the PaymentTransaction."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Returns all the fields from the SQLAlchemy class."""

        model = PaymentTransaction
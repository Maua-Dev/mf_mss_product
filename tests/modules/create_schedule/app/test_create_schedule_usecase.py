import pytest

from datetime import time

from src.modules.create_schedule.app.create_schedule_usecase import CreateScheduleUsecase

from src.shared.domain.enums.restaurant_enum import RESTAURANT
from src.shared.domain.enums.role_enum import ROLE

from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed

from src.shared.infra.repositories.order_repository_mock import OrderRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_CreateScheduleUseCase:
    def test_create_schedule_usecase(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_order, repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER  
        user.restaurant = RESTAURANT.CANTINA_DO_MOLEZA  
        
        create_schedule = usecase.__call__(
            schedule_id='c78f7935-6cdd-48cf-af87-b6163bcd59a8',
            initial_time=time(hour=10, minute=0),
            end_time=time(hour=11, minute=30),
            restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
            accepted_reservation=True,
            user_id=user.user_id
        )

        assert repo_order.schedules[-1].schedule_id == create_schedule.schedule_id
        assert repo_order.schedules[-1].initial_time == create_schedule.initial_time
        assert repo_order.schedules[-1].end_time == create_schedule.end_time
        assert repo_order.schedules[-1].restaurant == create_schedule.restaurant
        assert repo_order.schedules[-1].accepted_reservation == create_schedule.accepted_reservation
        assert repo_user.users_list[0].user_id == user.user_id


    def test_create_schedule_usecase_user_role_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_order, repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.USER
        user.restaurant = RESTAURANT.CANTINA_DO_MOLEZA

        with pytest.raises(UserNotAllowed):
            usecase.__call__(
                schedule_id='c78f7935-6cdd-48cf-af87-b6163bcd59a8',
                initial_time=time(hour=10, minute=0),
                end_time=time(hour=11, minute=30),
                restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
                accepted_reservation=True,
                user_id=user.user_id
            )
    
    def test_create_schedule_usecase_user_not_registered(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_order, repo_user)

        with pytest.raises(UnregisteredUser):
            usecase.__call__(
                schedule_id='c78f7935-6cdd-48cf-af87-b6163bcd59a8',
                initial_time=time(hour=10, minute=0),
                end_time=time(hour=11, minute=30),
                restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
                accepted_reservation=True,
                user_id='c78f7935-6cdd-48cf-af87-b6163bcd59a8'
            )

    def test_create_schedule_usecase_user_not_allowed(self):
        repo_order = OrderRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateScheduleUsecase(repo_order, repo_user)

        user = repo_user.users_list[0]
        user.role = ROLE.OWNER
        user.restaurant = None

        with pytest.raises(UserNotAllowed):
            usecase.__call__(
                schedule_id='c78f7935-6cdd-48cf-af87-b6163bcd59a8',
                initial_time=time(hour=10, minute=0),
                end_time=time(hour=11, minute=30),
                restaurant=RESTAURANT.CANTINA_DO_MOLEZA,
                accepted_reservation=True,
                user_id=user.user_id
            )

    
    

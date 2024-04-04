import { Module } from '@nestjs/common';
import { UserService } from './services/user.service';
import { UserRepository } from './repositories/user.repository';

@Module({
  imports: [],
  controllers: [],
  providers: [UserService, UserRepository],
  exports: [UserService, UserRepository],
})
export class UserModule {}

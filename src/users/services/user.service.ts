import { Injectable } from '@nestjs/common';
import { UserRepository } from '../repositories/user.repository';

@Injectable()
export class UserService {
  constructor(private readonly userRepository: UserRepository) {}

  createUser(stdNum: string, password: string) {
    return this.userRepository.createUser(stdNum, password);
  }
}

import graphene
from ponto.vendor import pavlok
from ponto.api import types
from ponto.db import functions


class PavlokAddKey(graphene.Mutation):
	class Input:
		client_id = graphene.NonNull(graphene.ID)
		client_secret = graphene.NonNull(graphene.ID)
		callback_url = graphene.NonNull(graphene.String)
		code = graphene.NonNull(graphene.ID)

	pavlok_key = graphene.Field(graphene.NonNull(types.PavlokKey))

	@staticmethod
	def mutate(root, args, context, info):
		pavlok_key = functions.create_pavlok_key(
			root.user_id,
			args.get('client_id'),
			args.get('client_secret'),
			args.get('callback_url'),
			args.get('code')
		)
		return PavlokAddKey(pavlok_key=pavlok_key)


class Shock(graphene.Mutation):
	"""
	Generates a shock stimulus for the associated Pavlok Device
	"""
	class Input:
		value = graphene.NonNull(graphene.Int)
		reason = graphene.String()

	success = graphene.NonNull(graphene.Boolean)

	@staticmethod
	def mutate(root, args, context, info):
		pavlok.shock(str(root.access_token), args.get('value'), reason=args.get('reason', None))
		return Shock(success=True)


class Beep(graphene.Mutation):
	"""
	Generates a beep stimulus for the associated Pavlok Device
	"""
	class Input:
		value = graphene.NonNull(graphene.Int)
		reason = graphene.String()

	success = graphene.NonNull(graphene.Boolean)

	@staticmethod
	def mutate(root, args, context, info):
		pavlok.beep(str(root.access_token), args.get('value'), reason=args.get('reason', None))
		return Beep(success=True)


class Vibration(graphene.Mutation):
	"""
	Generates a vibration stimulus for the associated Pavlok Device
	"""
	class Input:
		value = graphene.NonNull(graphene.Int)
		reason = graphene.String()

	success = graphene.NonNull(graphene.Boolean)

	@staticmethod
	def mutate(root, args, context, info):
		pavlok.vibration(str(root.access_token), args.get('value'), reason=args.get('reason', None))
		return Vibration(success=True)


class LED(graphene.Mutation):
	"""
	Generates a LED stimulus for the associated Pavlok Device
	"""
	class Input:
		value = graphene.NonNull(graphene.Int)
		reason = graphene.String()

	success = graphene.NonNull(graphene.Boolean)

	@staticmethod
	def mutate(root, args, context, info):
		pavlok.led(str(root.access_token), args.get('value'), reason=args.get('reason', None))
		return LED(success=True)


class RequestStimuli(graphene.ObjectType):
	"""
	Stimuli that you can call go here
	"""
	access_token = graphene.NonNull(graphene.ID)
	shock = Shock.Field()
	beep = Beep.Field()
	vibration = Vibration.Field()
	led = LED.Field()


class MutatePavlok(graphene.ObjectType):
	"""
	Pavlok Related Mutations go under here
	"""
	user_id = graphene.NonNull(graphene.ID)

	pavlok_add_key = PavlokAddKey.Field()
	request_stimuli = graphene.Field(graphene.NonNull(RequestStimuli), key_id=graphene.NonNull(graphene.ID))

	def resolve_request_stimuli(self, args, context, info):
		access_token = functions.pavlok_get_access_token_from_key_id(args.get('key_id'))
		return RequestStimuli(access_token=access_token)
